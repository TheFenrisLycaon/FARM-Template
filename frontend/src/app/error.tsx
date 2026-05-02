"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <main className="max-w-3xl mx-auto px-6 pt-28 pb-16">
      <h1 className="text-3xl font-semibold mb-4">Something went wrong</h1>
      <p className="text-gray-600 mb-6">{error.message}</p>
      <button
        onClick={reset}
        className="rounded-lg bg-purple-900 text-white px-4 py-2 hover:bg-purple-800"
      >
        Try again
      </button>
    </main>
  );
}
