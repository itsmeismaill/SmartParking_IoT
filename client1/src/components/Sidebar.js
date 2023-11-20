// Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <div className="bg-gray-800 text-white h-screen p-4">
      <Link to="/dashboard" className="block py-2 px-4">Dashboard</Link>
      <Link to="/dashboard/home" className="block py-2 px-4">Home</Link>
      <Link to="/dashboard/users" className="block py-2 px-4">Users</Link>
      {/* Add more links for other dashboard pages */}
    </div>
  );
};

export default Sidebar;
