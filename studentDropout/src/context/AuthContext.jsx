import React, { createContext, useContext, useState, useEffect } from "react";
import api from "../api/client";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    try {
      const savedUser = localStorage.getItem("user");
      return savedUser ? JSON.parse(savedUser) : null;
    } catch {
      return null;
    }
  });

  const [token, setToken] = useState(() => localStorage.getItem("token") || null);
  const [loading, setLoading] = useState(false);

  const isLoggedIn = !!token && !!user;
  const role = user?.role || null;

  // Validate active session against backend on load to eliminate zombie sessions if DB was wiped
  useEffect(() => {
    if (!token) return;

    let isMounted = true;
    const verifySession = async () => {
      try {
        const res = await api.get("/api/auth/me");
        if (isMounted && res.data?.user) {
          setUser((prev) => {
            const merged = { ...prev, ...res.data.user };
            localStorage.setItem("user", JSON.stringify(merged));
            return merged;
          });
        }
      } catch (err) {
        if (isMounted && (err.response?.status === 401 || err.response?.status === 404)) {
          console.warn("User session expired or user deleted from database. Clearing local session.");
          logout();
        }
      }
    };

    verifySession();
    return () => {
      isMounted = false;
    };
  }, [token]);

  const login = (userData, userToken) => {
    setUser(userData);
    setToken(userToken);
    localStorage.setItem("user", JSON.stringify(userData));
    localStorage.setItem("token", userToken);
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem("user");
    localStorage.removeItem("token");
  };

  const updateUser = (updatedFields) => {
    setUser((prev) => {
      const updated = { ...prev, ...updatedFields };
      localStorage.setItem("user", JSON.stringify(updated));
      return updated;
    });
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        role,
        isLoggedIn,
        loading,
        login,
        logout,
        updateUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
