import { useState, useEffect } from 'react';
import axiosClient from '../api/axiosClient';
import Header from '../components/Header';
import FilterBar from '../components/FilterBar';
import NoteCard from '../components/NoteCard';
import NoteForm from '../components/NoteForm';
import { Plus } from 'lucide-react';

const Notes = () => {
    const [notes, setNotes] = useState([]);
    const [filter, setFilter] = useState('Todas');
    const [isCreating, setIsCreating] = useState(false);
    const [editingNote, setEditingNote] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchNotes();
    }, []);

    const fetchNotes = async () => {
        try {
            setLoading(true);
            const response = await axiosClient.get('/notes');
            // Ensure notes is an array
            setNotes(Array.isArray(response.data) ? response.data : []);
            setError(null);
        } catch (err) {
            console.error('Error fetching notes:', err);
            setError('Could not load notes. Ensure the API is running.');
        } finally {
            setLoading(false);
        }
    };

    const handleCreate = async (noteData) => {
        try {
            const response = await axiosClient.post('/notes', noteData);
            setNotes((prev) => [response.data, ...prev]);
            setIsCreating(false);
        } catch (err) {
            console.error('Error creating note:', err);
            // Fallback for demo if needed, but alerting is safer
            alert('Failed to create note. API error.');
        }
    };

    const handleUpdate = async (noteData) => {
        try {
            const response = await axiosClient.put(`/notes/${noteData.id}`, noteData);
            setNotes((prev) => prev.map(n => n.id === noteData.id ? response.data : n));
            setEditingNote(null);
        } catch (err) {
            console.error('Error updating note:', err);
            alert('Failed to update note. API error.');
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm('Are you sure you want to delete this note?')) return;
        try {
            await axiosClient.delete(`/notes/${id}`);
            setNotes((prev) => prev.filter(n => n.id !== id));
        } catch (err) {
            console.error('Error deleting note:', err);
            alert('Failed to delete note. API error.');
        }
    };

    const filteredNotes = filter === 'Todas'
        ? notes
        : notes.filter(n => n.category === filter);

    return (
        <div className="min-h-screen bg-gray-50 flex flex-col">
            <Header />

            <main className="flex-1 max-w-7xl w-full mx-auto p-4">
                <div className="flex flex-col sm:flex-row justify-between items-center mb-6 gap-4">
                    <FilterBar currentFilter={filter} onFilterChange={setFilter} />

                    {!isCreating && !editingNote && (
                        <button
                            onClick={() => setIsCreating(true)}
                            className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 transition w-full sm:w-auto justify-center"
                        >
                            <Plus size={20} />
                            <span>New Note</span>
                        </button>
                    )}
                </div>

                {error && <div className="text-red-700 bg-red-100 p-4 rounded mb-6 border border-red-200">{error}</div>}

                {(isCreating || editingNote) && (
                    <NoteForm
                        initialData={editingNote}
                        onSubmit={editingNote ? handleUpdate : handleCreate}
                        onCancel={() => {
                            setIsCreating(false);
                            setEditingNote(null);
                        }}
                    />
                )}

                {loading ? (
                    <div className="flex justify-center py-20">
                        <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600"></div>
                    </div>
                ) : (
                    <div className={`transition-opacity duration-300 ${isCreating || editingNote ? 'opacity-50 pointer-events-none' : 'opacity-100'}`}>
                        {filteredNotes.length === 0 ? (
                            <div className="text-center py-20 text-gray-500">
                                {filter === 'Todas' ? (
                                    <div className="flex flex-col items-center">
                                        <p className="mb-2">You don't have any notes yet.</p>
                                        <button onClick={() => setIsCreating(true)} className="text-blue-600 hover:underline">Create one now</button>
                                    </div>
                                ) : `No notes found in ${filter}.`}
                            </div>
                        ) : (
                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                                {filteredNotes.map(note => (
                                    <NoteCard
                                        key={note.id}
                                        note={note}
                                        onEdit={setEditingNote}
                                        onDelete={handleDelete}
                                    />
                                ))}
                            </div>
                        )}
                    </div>
                )}
            </main>
        </div>
    );
};

export default Notes;
