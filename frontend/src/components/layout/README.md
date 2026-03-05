# Layout Components

This folder contains layout components (header, footer, navigation, containers).

## Adding Layout Frames from Figma

When you get a Figma frame for a layout component:

1. **Identify the layout component:**
   - Header/Navigation bar
   - Footer
   - Sidebar
   - Container/Wrapper
   - Grid/List layouts

2. **Create the component:**
   ```
   Header.jsx
   Footer.jsx
   Navigation.jsx
   ```

3. **Match Figma structure:**
   - Use the same HTML structure as the Figma frame
   - Match spacing, colors, and typography
   - Implement responsive breakpoints if Figma has them

4. **Example:**
   ```jsx
   // Header.jsx
   // Figma Frame: "Desktop Header"
   
   export default function Header() {
     return (
       <header className="[Figma-matched classes]">
         <nav>
           {/* Navigation items */}
         </nav>
       </header>
     );
   }
   ```
