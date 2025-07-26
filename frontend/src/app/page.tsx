import WelcomePage from '@/welcome';
import { auth, currentUser } from '@clerk/nextjs/server';

export default async function Home() {
  const { userId } = await auth()

  if (!userId) {
    return (
      <WelcomePage />
    )
  }

  const user = await currentUser()

  return (
    <>
      <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b text-white pt-24 px-4">
        <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
          Hello, {user ? user.firstName : 'Guest'}!
          <div className="flex gap-4 items-center flex-col sm:flex-row">
          </div>
        </main>
      </div>
    </>
  );
}