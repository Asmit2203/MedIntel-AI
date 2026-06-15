/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#2563eb",
        secondary: "#0f172a",
        success: "#22c55e",
        warning: "#f59e0b",
        danger: "#ef4444"
      }
    }
  },
  plugins: []
}