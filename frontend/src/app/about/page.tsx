export const metadata = {
  title: "About — FARM Template",
};

export default function AboutPage() {
  return (
    <main className="max-w-3xl mx-auto px-6 pt-28 pb-16">
      <h1 className="text-3xl font-semibold mb-4">About</h1>
      <p className="text-gray-600">
        FARM Template is a starter combining FastAPI, MongoDB (via Beanie),
        Next.js, Tailwind, and Clerk authentication.
      </p>
    </main>
  );
}
