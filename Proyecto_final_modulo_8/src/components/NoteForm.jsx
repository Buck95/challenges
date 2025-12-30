import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

const categories = ['Personal', 'Trabajo', 'Ideas', 'Recordatorios'];

const NoteForm = ({ initialData, onSubmit, onCancel }) => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [category, setCategory] = useState(categories[0]);

    useEffect(() => {
        if (initialData) {
            setTitle(initialData.title);
            setContent(initialData.content);
            setCategory(initialData.category);
        } else {
            setTitle('');
            setContent('');
            setCategory(categories[0]);
        }
    }, [initialData]);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({
            id: initialData?.id,
            title,
            content,
            category,
            date: initialData?.date || new Date().toISOString()
        });
    };

    return (
        <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md mb-6 border border-gray-100 animate-in fade-in slide-in-from-top-4 duration-300">
            <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold text-gray-800">{initialData ? 'Edit Note' : 'New Note'}</h3>
                <button type="button" onClick={onCancel} className="text-gray-500 hover:text-gray-700 text-sm">Cancel</button>
            </div>

            <div className="mb-4">
                <input
                    type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 transition-shadow"
                />
            </div>

            <div className="mb-4">
                <textarea
                    placeholder="Write your note here..."
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                    rows="4"
                    className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none transition-shadow"
                />
            </div>

            <div className="flex gap-4 items-center flex-wrap">
                <select
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
                >
                    {categories.map(cat => <option key={cat} value={cat}>{cat}</option>)}
                </select>

                <button
                    type="submit"
                    className="ml-auto bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors font-medium shadow-sm"
                >
                    {initialData ? 'Update Note' : 'Create Note'}
                </button>
            </div>
        </form>
    );
};

NoteForm.propTypes = {
    initialData: PropTypes.object,
    onSubmit: PropTypes.func.isRequired,
    onCancel: PropTypes.func.isRequired,
};

export default NoteForm;
