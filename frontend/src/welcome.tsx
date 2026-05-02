const FEATURES = [
    {
        title: "Full Stack Template",
        description: "Includes a Next.js frontend and a FastAPI backend for rapid development."
    },
    {
        title: "Authentication",
        description: "Integrated with Clerk for seamless user authentication and management."
    },
    {
        title: "API Ready",
        description: "Backend is structured for scalable API development with FastAPI."
    },
    {
        title: "Modern UI",
        description: "Styled with Tailwind CSS for a clean, responsive interface."
    },
    {
        title: "Docker Support",
        description: "Easy deployment and local development with Docker."
    },
    {
        title: "TypeScript & Linting",
        description: "Type safety and code quality enforced throughout the project."
    },
];

const WelcomePage = () => {
    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-purple-900 to-purple-600 text-white pt-24 px-4">
            <h1 className="text-4xl font-bold mb-4">Welcome to the FARM Template!</h1>
            <p className="mb-8 text-lg max-w-2xl text-center">
                This project provides a modern, production-ready full stack template combining Next.js and FastAPI, designed to help you build and scale your applications quickly.
            </p>
            <div className="w-full max-w-3xl grid grid-cols-1 md:grid-cols-2 gap-6">
                {FEATURES.map((feature, idx) => (
                    <div key={idx} className="card bg-purple-800 bg-opacity-80 rounded-lg p-6 shadow-md border border-pink-300">
                        <h2 className="text-2xl font-semibold mb-2">{feature.title}</h2>
                        <p className="text-base text-purple-100">{feature.description}</p>
                    </div>
                ))}
            </div>
            <div className="mt-10 text-center p-20">
                <p className="text-md">Get started by exploring the navigation bar above.</p>
            </div>
        </div>
    );
};

export default WelcomePage;
