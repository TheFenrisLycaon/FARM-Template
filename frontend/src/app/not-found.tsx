import Link from "next/link";

export default function NotFound() {
  return (
    <main className="max-w-3xl mx-auto px-6 pt-28 pb-16">
      <h1 className="text-3xl font-semibold mb-4">Page not found</h1>
      <p className="text-gray-600 mb-6">
        The page you&apos;re looking for doesn&apos;t exist.
      </p>
      <Link href="/" className="text-purple-900 underline">
        Go home
      </Link>
    </main>
  );
}
