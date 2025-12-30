import { createContext, useContext, useState, useEffect } from 'react';
import axiosClient from '../api/axiosClient';
import PropTypes from 'prop-types';

const AuthContext = createContext({
    user: null,
    token: null,
    login: async () => { },
    register: async () => { },
    logout: () => { },
    isAuthenticated: false,
});

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem('token'));

    useEffect(() => {
        if (token) {
            localStorage.setItem('token', token);
            // Ideally fetch user profile here if token exists but user is null
        } else {
            localStorage.removeItem('token');
            setUser(null);
        }
    }, [token]);

    const login = async (email, password) => {
        try {
            const response = await axiosClient.post('/login', { email, password });
            // Assuming API returns { accessToken: "...", user: { ... } }
            const { accessToken, user } = response.data;
            setToken(accessToken);
            setUser(user);
            return true;
        } catch (error) {
            console.error("Login failed", error);
            throw error;
        }
    };

    const register = async (name, email, password) => {
        try {
            const response = await axiosClient.post('/register', { email, password, name });
            const { accessToken, user } = response.data;
            setToken(accessToken);
            setUser(user);
            return true;
        } catch (error) {
            console.error("Registration failed", error);
            throw error;
        }
    };

    const logout = () => {
        setToken(null);
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{
            user,
            token,
            login,
            register,
            logout,
            isAuthenticated: !!token
        }}>
            {children}
        </AuthContext.Provider>
    );
};

AuthProvider.propTypes = {
    children: PropTypes.node.isRequired,
};

export default AuthContext;
