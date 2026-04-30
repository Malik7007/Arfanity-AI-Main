<script>
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { AI_NAME } from '$lib/stores';
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-50 dark:bg-gray-950 p-4 transition-colors duration-300">
	<div class="max-w-md w-full text-center space-y-8">
		<div class="relative inline-block">
			<div class="absolute -inset-4 bg-linear-to-r from-blue-600 to-indigo-600 rounded-full blur-2xl opacity-20 animate-pulse"></div>
			<h1 class="relative text-9xl font-black text-gray-200 dark:text-gray-800 tracking-tighter">
				{$page.status}
			</h1>
		</div>
		
		<div class="space-y-4 relative">
			<h2 class="text-3xl font-bold text-gray-900 dark:text-white">
				{$page.error?.message || 'Something went wrong'}
			</h2>
			<p class="text-gray-500 dark:text-gray-400 text-lg">
				We apologize for the inconvenience. Our team has been notified and is working to resolve the issue.
			</p>
		</div>

		<div class="flex flex-col sm:flex-row gap-4 justify-center items-center pt-4">
			<button
				on:click={() => goto('/')}
				class="px-8 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-2xl shadow-lg shadow-blue-500/25 transition-all hover:scale-105 active:scale-95 flex items-center gap-2"
			>
				Back to Home
			</button>
			<button
				on:click={() => window.location.reload()}
				class="px-8 py-3 bg-gray-200 dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 text-gray-900 dark:text-white font-semibold rounded-2xl transition-all hover:scale-105 active:scale-95"
			>
				Try Again
			</button>
		</div>

		<div class="pt-12">
			<p class="text-sm text-gray-400 dark:text-gray-600 uppercase tracking-widest font-bold">
				{$AI_NAME} Core
			</p>
		</div>
	</div>
</div>
