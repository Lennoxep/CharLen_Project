/**
 * FIGMA FRAME TEMPLATE
 * 
 * Use this template when converting a Figma frame into a React component.
 * 
 * Instructions:
 * 1. Copy this file and rename it to match your Figma frame name
 * 2. Replace the placeholder content with your Figma design
 * 3. Match the Tailwind classes to your Figma measurements
 * 4. Export any assets (images, icons) to src/assets/
 */

export default function FigmaFrameTemplate() {
  return (
    <div className="[Match Figma container styles]">
      {/* 
        STEP 1: Look at your Figma frame structure
        - What's the main container? (div, section, etc.)
        - What are the child elements?
        
        STEP 2: Match measurements from Figma Inspect panel
        - Width/Height → w-[value] or h-[value]
        - Padding → p-[value] or px-[value] py-[value]
        - Margin → m-[value] or mx-[value] my-[value]
        - Gap → gap-[value]
        
        STEP 3: Match colors from Figma
        - Background → bg-[color] (use design tokens if possible)
        - Text → text-[color]
        - Border → border-[color]
        
        STEP 4: Match typography from Figma
        - Font size → text-[size]
        - Font weight → font-[weight]
        - Line height → leading-[value]
        
        STEP 5: Match effects from Figma
        - Border radius → rounded-[value]
        - Shadows → shadow-[value]
        - Opacity → opacity-[value]
      */}
      
      {/* Example structure - replace with your Figma frame */}
      <div className="w-full max-w-5xl mx-auto p-6">
        <h1 className="text-4xl font-bold mb-4">
          {/* Match Figma heading styles */}
        </h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Match Figma grid/auto-layout */}
        </div>
      </div>
    </div>
  );
}

/**
 * FIGMA MEASUREMENT CHEAT SHEET:
 * 
 * Common Figma → Tailwind conversions:
 * 
 * Spacing:
 * - 4px = p-1, m-1, gap-1
 * - 8px = p-2, m-2, gap-2
 * - 16px = p-4, m-4, gap-4
 * - 24px = p-6, m-6, gap-6
 * - 32px = p-8, m-8, gap-8
 * 
 * Border Radius:
 * - 4px = rounded
 * - 8px = rounded-lg
 * - 12px = rounded-xl
 * - 16px = rounded-2xl
 * - 9999px = rounded-full
 * 
 * Typography:
 * - 12px = text-xs
 * - 14px = text-sm
 * - 16px = text-base
 * - 18px = text-lg
 * - 20px = text-xl
 * - 24px = text-2xl
 * - 30px = text-3xl
 * - 36px = text-4xl
 * 
 * Colors:
 * - Use design tokens: var(--color-primary)
 * - Or Tailwind: bg-blue-500, text-gray-600
 * - Or exact: bg-[#646cff]
 */
