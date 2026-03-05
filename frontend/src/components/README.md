# Components Directory

This directory is organized to make it easy to add Figma frames as React components.

## 📁 Folder Structure

```
components/
├── ui/              # Reusable UI components (buttons, inputs, cards, badges)
├── layout/          # Layout components (header, footer, navigation, containers)
├── features/        # Feature-specific components (book-related, user-related, etc.)
└── README.md        # This file
```

## 🎨 Adding a Figma Frame

### Quick Start

1. **Identify the component type:**
   - **UI component** → `components/ui/`
   - **Layout component** → `components/layout/`
   - **Feature component** → `components/features/`

2. **Copy the template:**
   ```bash
   cp components/FIGMA_FRAME_TEMPLATE.jsx components/ui/YourComponentName.jsx
   ```

3. **Open Figma and get measurements:**
   - Select the frame
   - Open the **Inspect panel** (right sidebar)
   - Note: width, height, padding, margin, colors, fonts

4. **Convert to React:**
   - Match structure (divs, sections, etc.)
   - Use Tailwind classes for styling
   - Reference `src/styles/design-tokens.css` for colors/spacing

5. **Export assets:**
   - Images/icons → `src/assets/`
   - Fonts → `src/assets/fonts/`

## 📐 Component Organization

### UI Components (`ui/`)
Small, reusable pieces:
- `Button.jsx`
- `Input.jsx`
- `Card.jsx`
- `Badge.jsx`
- `Modal.jsx`

### Layout Components (`layout/`)
Page structure:
- `Header.jsx`
- `Footer.jsx`
- `Navigation.jsx`
- `Container.jsx`
- `Sidebar.jsx`

### Feature Components (`features/`)
Domain-specific:
- `BookCard.jsx` (already exists!)
- `BookList.jsx`
- `UserProfile.jsx`
- etc.

## 🔗 Integration with App.jsx

After creating a component from a Figma frame:

```jsx
// In App.jsx or any other component
import YourComponent from './components/ui/YourComponent';

function App() {
  return (
    <div>
      <YourComponent />
    </div>
  );
}
```

## 📚 Resources

- See `FIGMA_FRAME_TEMPLATE.jsx` for a detailed template
- See `../FIGMA_INTEGRATION.md` for the full guide
- Check `../styles/design-tokens.css` for design system values
