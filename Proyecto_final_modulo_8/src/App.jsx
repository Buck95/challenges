import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import ProtectedRoute from './routes/ProtectedRoute';
import Login from './pages/Login';
import Register from './pages/Register';
import Notes from './pages/Notes';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route element={<ProtectedRoute />}>
            <Route path="/notes" element={<Notes />} />
            <Route path="/" element={<Navigate to="/notes" replace />} />
          </Route>

          <Route path="*" element={<Navigate to="/notes" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
