import PropTypes from 'prop-types';
import clsx from 'clsx';

const categories = ['Todas', 'Personal', 'Trabajo', 'Ideas', 'Recordatorios'];

const FilterBar = ({ currentFilter, onFilterChange }) => {
    return (
        <div className="flex flex-wrap gap-2 mb-6">
            {categories.map((cat) => (
                <button
                    key={cat}
                    onClick={() => onFilterChange(cat)}
                    className={clsx(
                        'px-4 py-2 rounded-full text-sm font-medium transition-colors border',
                        currentFilter === cat
                            ? 'bg-gray-800 text-white border-gray-800'
                            : 'bg-white text-gray-600 border-gray-300 hover:bg-gray-100'
                    )}
                >
                    {cat}
                </button>
            ))}
        </div>
    );
};

FilterBar.propTypes = {
    currentFilter: PropTypes.string.isRequired,
    onFilterChange: PropTypes.func.isRequired,
};

export default FilterBar;
