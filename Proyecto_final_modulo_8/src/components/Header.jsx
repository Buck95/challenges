import { useAuth } from '../contexts/AuthContext';
import { LogOut } from 'lucide-react';
import { Link } from 'react-router-dom';

const Header = () => {
    const { user, logout } = useAuth();

    return (
        <header className="bg-white shadow-sm sticky top-0 z-10">
            <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
                <Link to="/notes" className="text-xl font-bold text-gray-800 tracking-tight">MyNotes</Link>
                <div className="flex items-center gap-4">
                    <span className="text-gray-600 text-sm hidden sm:block">Welcome, {user?.name || user?.email || 'User'}</span>
                    <button
                        onClick={logout}
                        className="flex items-center gap-2 text-gray-600 hover:text-red-600 transition-colors"
                        title="Logout"
                    >
                        <LogOut size={20} />
                        <span className="hidden sm:inline">Logout</span>
                    </button>
                </div>
            </div>
        </header>
    );
};

export default Header;
