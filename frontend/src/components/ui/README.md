# UI Components

This folder contains reusable UI components that match your Figma design system.

## Adding Components from Figma

When you get a Figma frame for a UI component (button, input, card, etc.):

1. **Create a new file** with the component name:
   ```
   Button.jsx
   Input.jsx
   Card.jsx
   ```

2. **Use this template:**
   ```jsx
   // ComponentName.jsx
   // Description: [What this component does]
   // Figma Frame: [Link or name of Figma frame]
   
   export default function ComponentName({ prop1, prop2 }) {
     return (
       <div className="[Tailwind classes matching Figma]">
         {/* Component content */}
       </div>
     );
   }
   ```

3. **Match Figma styles:**
   - Use Tailwind classes for spacing, colors, typography
   - Reference `design-tokens.css` for custom values
   - Use Figma's Inspect panel for exact measurements

4. **Export and use:**
   ```jsx
   import ComponentName from './components/ui/ComponentName';
   ```
