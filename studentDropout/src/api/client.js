import axios from "axios";

// Derive backend URL from environment variable if present (e.g. on Vercel),
// or fallback to current browser host so other devices on the same
// Wi-Fi network can reach the backend automatically.
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  `http://${window.location.hostname}:5000`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Attach Authorization Bearer token dynamically to every request
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor to handle authentication errors gracefully
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const isAuthError =
      error.response &&
      (error.response.status === 401 ||
        (error.response.status === 404 &&
          typeof error.response.data?.message === "string" &&
          error.response.data.message.toLowerCase().includes("user not found")));

    if (isAuthError) {
      // Token expired, user deleted from DB, or invalid session - clear local session
      localStorage.removeItem("token");
      localStorage.removeItem("user");

      const pathname = window.location.pathname;
      if (pathname !== "/login" && pathname !== "/register") {
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  }
);

export default api;
