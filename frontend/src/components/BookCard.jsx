import React from "react";

// Simple presentational card for a book. Receives `book` and two handlers:
// `onLike` and `onDislike` which are called when the user clicks the buttons.
export default function BookCard({ book, onLike, onDislike }) {
  if (!book) return null;

  return (
    <div>
      {/* Placeholder cover area */}
      <div className="aspect-[3/4] w-full rounded-2xl bg-gray-100 flex items-center justify-center text-gray-400">
        <div className="text-center">Cover</div>
      </div>
      <div className="mt-4">
        <div className="text-lg font-semibold">{book.title}</div>
        <div className="text-sm text-gray-600">{book.author}</div>

        {/* Action buttons call the handlers passed from the parent `App` component */}
        <div className="mt-4 flex gap-3">
          <button
            className="flex-1 rounded-2xl border px-4 py-3 hover:bg-gray-50"
            onClick={onDislike}
            aria-label="Dislike"
          >
            Dislike
          </button>
          <button
            className="flex-1 rounded-2xl bg-black px-4 py-3 text-white hover:opacity-90"
            onClick={onLike}
            aria-label="Like"
          >
            Like
          </button>
        </div>
      </div>
    </div>
  );
}
