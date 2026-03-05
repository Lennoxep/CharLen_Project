import React, { useState } from "react";
import BookCard from "./components/BookCard";

export default function App() {
	// sampleBooks: small in-memory list used for this demo UI
	// In a real app this would come from an API or database
	const sampleBooks = [
		{ id: 1, title: "The Midnight Library", author: "Matt Haig" },
		{ id: 2, title: "1984", author: "George Orwell" },
		{ id: 3, title: "Dune", author: "Frank Herbert" },
	];

	// `index` tracks which book from `sampleBooks` is currently visible
	const [index, setIndex] = useState(0);
	// `likes` stores books the user tapped "Like" for during this session
	const [likes, setLikes] = useState([]);
	// `showLikes` controls whether the liked-books panel is visible
	const [showLikes, setShowLikes] = useState(false);

	const current = sampleBooks[index];

	// Called when the user presses the "Like" button on a card.
	// Adds the current book to `likes` then advances to the next book.
	function handleLike() {
		if (!current) return;
		setLikes((s) => [...s, current]);
		setIndex((i) => i + 1);
	}

	// Called when the user presses "Dislike" — simply advance to next book.
	function handleDislike() {
		if (!current) return;
		setIndex((i) => i + 1);
	}

	// Reset the demo state to the beginning
	function reset() {
		setIndex(0);
		setLikes([]);
		setShowLikes(false);
	}

	return (
		<div className="min-h-screen bg-white">
			{/* Top bar */}
			<header className="mx-auto flex w-full max-w-5xl items-center justify-between px-6 py-5">
				<div className="text-lg font-semibold">📚 Book Tinder</div>
				{/* sign-in button: placeholder for future auth flow */}
				<button className="rounded-xl border px-4 py-2 text-sm hover:bg-gray-50">Sign in</button>
			</header>

			{/* Hero */}
			<main className="mx-auto grid w-full max-w-5xl grid-cols-1 gap-10 px-6 py-10 md:grid-cols-2 md:items-center">
				<div>
					<h1 className="text-4xl font-bold leading-tight md:text-5xl">
						Discover books
						<span className="block">the fun way.</span>
					</h1>

					<p className="mt-4 text-base text-gray-600">
						Swipe through book cards. Like what you see. Build your next-read list.
					</p>

					<div className="mt-6 flex flex-col gap-3 sm:flex-row">
						{/* Reset starts the demo run; View your likes toggles the liked-list panel */}
						<button
							className="rounded-2xl bg-black px-6 py-3 text-white hover:opacity-90"
							onClick={reset}
						>
							Start swiping
						</button>
						<button
							className="rounded-2xl border px-6 py-3 hover:bg-gray-50"
							onClick={() => setShowLikes((s) => !s)}
						>
							View your likes ({likes.length})
						</button>
					</div>

					<p className="mt-4 text-sm text-gray-500">MVP: swipe + likes. Accounts & recommendations later.</p>

					{/* showLikes: when true, render a small list of liked books */}
					{showLikes && (
						<div className="mt-6 rounded-lg border p-4">
							<div className="mb-2 font-semibold">Liked books</div>
							{likes.length === 0 ? (
								<div className="text-sm text-gray-600">You haven't liked any books yet.</div>
							) : (
								<ul className="list-disc pl-5 text-sm">
									{likes.map((b) => (
										<li key={b.id} className="py-1">
											{b.title} <span className="text-gray-500">— {b.author}</span>
										</li>
									))}
								</ul>
							)}
						</div>
					)}
				</div>

				{/* Preview card */}
				<div className="flex justify-center md:justify-end">
					<div className="w-full max-w-sm rounded-3xl border p-5 shadow-sm">
						{current ? (
							<BookCard book={current} onLike={handleLike} onDislike={handleDislike} />
						) : (
							<div className="p-6 text-center">
								<div className="text-lg font-semibold">No more books</div>
								<p className="mt-2 text-sm text-gray-600">You've reached the end of the sample list.</p>
								<div className="mt-4 flex gap-3">
									<button
										className="flex-1 rounded-2xl border px-4 py-3 hover:bg-gray-50"
										onClick={() => setIndex(0)}
									>
										Start over
									</button>
									<button
										className="flex-1 rounded-2xl bg-black px-4 py-3 text-white hover:opacity-90"
										onClick={() => setShowLikes(true)}
									>
										View likes
									</button>
								</div>
							</div>
						)}
					</div>
				</div>
			</main>
		</div>
	);
}