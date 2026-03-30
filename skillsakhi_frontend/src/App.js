import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import AboutPage from './pages/AboutPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import RecommendationPage from './pages/RecommendationPage';
import DashboardPage from './pages/DashboardPage';

const App = () => (
  <div>
    <nav className="nav">
      <Link to="/">SkillSakhi</Link>
      <div>
        <Link to="/about">About</Link>
        <Link to="/register">Register</Link>
        <Link to="/login">Login</Link>
        <Link to="/profile">Profile</Link>
        <Link to="/recommendation">Recommendation</Link>
        <Link to="/dashboard">Dashboard</Link>
      </div>
    </nav>
    <main className="container">
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/recommendation" element={<RecommendationPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </main>
  </div>
);

export default App;
