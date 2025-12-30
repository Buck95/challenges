import PropTypes from 'prop-types';
import { Edit, Trash2 } from 'lucide-react';

const categoryColors = {
    Personal: 'border-blue-500 bg-blue-50',
    Trabajo: 'border-green-500 bg-green-50',
    Ideas: 'border-yellow-500 bg-yellow-50',
    Recordatorios: 'border-red-500 bg-red-50',
};

const badgeColors = {
    Personal: 'bg-blue-100 text-blue-800',
    Trabajo: 'bg-green-100 text-green-800',
    Ideas: 'bg-yellow-100 text-yellow-800',
    Recordatorios: 'bg-red-100 text-red-800',
};

const NoteCard = ({ note, onEdit, onDelete }) => {
    const { title, content, category, date } = note;

    return (
        <div className={`border-l-4 p-4 rounded shadow-sm hover:shadow-md transition-shadow bg-white ${categoryColors[category] || 'border-gray-500'}`}>
            <div className="flex justify-between items-start mb-2">
                <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
                <span className={`text-xs px-2 py-1 rounded-full font-medium ${badgeColors[category] || 'bg-gray-100 text-gray-800'}`}>
                    {category}
                </span>
            </div>
            <p className="text-gray-600 mb-4 whitespace-pre-wrap line-clamp-3">{content}</p>
            <div className="flex justify-between items-center text-sm text-gray-500">
                <span>{date ? new Date(date).toLocaleDateString() : 'No date'}</span>
                <div className="flex space-x-2">
                    <button onClick={() => onEdit(note)} className="p-1 hover:text-blue-600 transition-colors" title="Edit">
                        <Edit size={18} />
                    </button>
                    <button onClick={() => onDelete(note.id)} className="p-1 hover:text-red-600 transition-colors" title="Delete">
                        <Trash2 size={18} />
                    </button>
                </div>
            </div>
        </div>
    );
};

NoteCard.propTypes = {
    note: PropTypes.shape({
        id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
        title: PropTypes.string.isRequired,
        content: PropTypes.string.isRequired,
        category: PropTypes.string.isRequired,
        date: PropTypes.string,
    }).isRequired,
    onEdit: PropTypes.func.isRequired,
    onDelete: PropTypes.func.isRequired,
};

export default NoteCard;
