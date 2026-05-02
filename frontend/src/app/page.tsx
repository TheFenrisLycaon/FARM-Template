import WelcomePage from '@/welcome';
import { currentUser } from '@clerk/nextjs/server';

export default async function Home() {
  const user = await currentUser()

  if (!user) {
    return <WelcomePage />
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b text-white pt-24 px-4">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        Hello, {user.firstName}!
        <div className="flex gap-4 items-center flex-col sm:flex-row">
        </div>
      </main>
    </div>
  );
}