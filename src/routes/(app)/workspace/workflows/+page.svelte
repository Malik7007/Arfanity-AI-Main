<script lang="ts">
	import { onMount, getContext } from 'svelte';
	import { toast } from 'svelte-sonner';
	import { goto } from '$app/navigation';
	import { AI_NAME, mobile, showSidebar, user, config } from '$lib/stores';

	import Spinner from '$lib/components/common/Spinner.svelte';
	import Tooltip from '$lib/components/common/Tooltip.svelte';
	import Pagination from '$lib/components/common/Pagination.svelte';
	import Plus from '$lib/components/icons/Plus.svelte';
	import SidebarIcon from '$lib/components/icons/Sidebar.svelte';
	import Search from '$lib/components/icons/Search.svelte';
	import XMark from '$lib/components/icons/XMark.svelte';
	import EllipsisHorizontal from '$lib/components/icons/EllipsisHorizontal.svelte';
	import ChevronRight from '$lib/components/icons/ChevronRight.svelte';

	const i18n = getContext('i18n');

	let loaded = false;
	let workflows = [];
	let total = 0;
	let loading = false;
	let query = '';
	let page = 1;

	// Mock data for now until backend is ready
	const mockWorkflows = [
		{ id: '1', name: 'Customer Support Bot', description: 'Handles common customer inquiries using GPT-4 and Knowledge Base.', status: 'active', updated_at: Date.now() },
		{ id: '2', name: 'Daily News Summary', description: 'Fetches top news and summarizes them into a daily digest.', status: 'paused', updated_at: Date.now() - 86400000 }
	];

	const getWorkflows = async () => {
		loading = true;
		// TODO: Implement API call
		setTimeout(() => {
			workflows = mockWorkflows;
			total = workflows.length;
			loading = false;
			loaded = true;
		}, 500);
	};

	onMount(async () => {
		await getWorkflows();
	});
</script>

<svelte:head>
	<title>{$i18n.t('Workflows')} • {$AI_NAME}</title>
</svelte:head>

<div
	class="flex flex-col w-full h-screen max-h-[100dvh] transition-width duration-200 ease-in-out {$showSidebar
		? 'md:max-w-[calc(100%-var(--sidebar-width))]'
		: ''} max-w-full"
>
	<div class="flex-1 max-h-full overflow-y-auto">
		<div class="pb-1 px-3 md:px-[18px] pt-2">
			<div class="flex flex-col gap-1 px-1 mt-1.5 mb-3">
				<div class="flex justify-between items-center">
					<div class="flex items-center md:self-center text-xl font-medium px-0.5 gap-2 shrink-0">
						{#if $mobile}
							<button
								id="sidebar-toggle-button"
								class="cursor-pointer flex rounded-lg hover:bg-gray-100 dark:hover:bg-gray-850 transition"
								on:click={() => {
									showSidebar.set(!$showSidebar);
								}}
							>
								<div class="self-center p-1.5">
									<SidebarIcon />
								</div>
							</button>
						{/if}
						<div>{$i18n.t('Workflows')}</div>
						<div class="text-lg font-medium text-gray-500 dark:text-gray-500">
							{total || ''}
						</div>
					</div>

					<div class="flex w-full justify-end gap-1.5">
						<button
							class="px-2 py-1.5 rounded-xl bg-black text-white dark:bg-white dark:text-black transition font-medium text-sm flex items-center"
							on:click={() => {
								goto('/workspace/workflows/create');
							}}
						>
							<Plus className="size-3" strokeWidth="2.5" />
							<div class="hidden md:block md:ml-1 text-xs">
								{$i18n.t('New Workflow')}
							</div>
						</button>
					</div>
				</div>
			</div>

			<div
				class="py-2 bg-white dark:bg-gray-900 rounded-3xl border border-gray-100/30 dark:border-gray-850/30"
			>
				<div class="px-3.5 flex flex-1 items-center w-full space-x-2 py-0.5 pb-2">
					<div class="flex flex-1 items-center">
						<div class="self-center ml-1 mr-3">
							<Search className="size-3.5" />
						</div>
						<input
							class="w-full text-sm py-1 rounded-r-xl outline-hidden bg-transparent"
							bind:value={query}
							placeholder={$i18n.t('Search Workflows')}
						/>
					</div>
				</div>

				{#if !loaded || loading}
					<div class="w-full h-full flex justify-center items-center my-16 mb-24">
						<Spinner className="size-5" />
					</div>
				{:else if workflows.length === 0}
					<div class="w-full h-full flex flex-col justify-center items-center my-16 mb-24">
						<div class="max-w-md text-center">
							<div class="text-3xl mb-3">🧠</div>
							<div class="text-lg font-medium mb-1">{$i18n.t('No workflows found')}</div>
							<div class="text-gray-500 text-center text-xs">
								{$i18n.t('Create visual AI pipelines to automate your tasks.')}
							</div>
						</div>
					</div>
				{:else}
					<div class="gap-2 grid my-2 px-3">
						{#each workflows as workflow (workflow.id)}
							<button
								class="flex space-x-4 text-left w-full px-3 py-3 dark:hover:bg-gray-850/50 hover:bg-gray-50 transition rounded-2xl group"
								on:click={() => {
									goto(`/workspace/workflows/edit?id=${workflow.id}`);
								}}
							>
								<div class="flex-1">
									<div class="flex items-center gap-2">
										<div class="line-clamp-1 text-sm font-medium">{workflow.name}</div>
										{#if workflow.status === 'active'}
											<span class="size-1.5 rounded-full bg-green-500"></span>
										{:else}
											<span class="size-1.5 rounded-full bg-gray-400"></span>
										{/if}
									</div>
									<div class="text-xs text-gray-500 line-clamp-1 mt-0.5">
										{workflow.description}
									</div>
								</div>

								<div class="flex flex-row gap-0.5 self-center">
									<div class="text-gray-300 group-hover:text-gray-600 dark:group-hover:text-gray-400 transition">
										<ChevronRight className="size-4" />
									</div>
								</div>
							</button>
						{/each}
					</div>
				{/if}
			</div>
		</div>
	</div>
</div>
