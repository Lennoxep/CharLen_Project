/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // Customize these to match your Figma design system
      colors: {
        // You can add custom colors here that match Figma
        // Example: 'primary': '#646cff',
      },
      fontFamily: {
        // Add your Figma font families here
        // Example: 'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      spacing: {
        // Add custom spacing if needed to match Figma
      },
      borderRadius: {
        // Add custom border radius values from Figma
      },
    },
  },
  plugins: [],
}
