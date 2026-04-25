<script lang="ts">
	import { toast } from 'svelte-sonner';
	import { goto } from '$app/navigation';
	import { getContext } from 'svelte';
	import WorkflowEditor from '$lib/components/workspace/Workflows/WorkflowEditor.svelte';
	import { mobile, showSidebar } from '$lib/stores';

	const i18n = getContext('i18n');

	const onSave = async (data) => {
		console.log('Saving workflow:', data);
		// TODO: Implement actual API save
		toast.success($i18n.t('Workflow created successfully'));
		goto('/workspace/workflows');
	};
</script>

<svelte:head>
	<title>{$i18n.t('Create Workflow')} • Arfanity AI</title>
</svelte:head>

<div
	class="flex flex-col w-full h-screen max-h-[100dvh] transition-width duration-200 ease-in-out {$showSidebar
		? 'md:max-w-[calc(100%-var(--sidebar-width))]'
		: ''} max-w-full"
>
	<div class="flex-1 w-full h-full relative">
		<WorkflowEditor {onSave} />
	</div>
</div>
