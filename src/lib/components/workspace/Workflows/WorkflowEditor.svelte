<script lang="ts">
	import { onMount, getContext, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';
	import {
		SvelteFlow,
		Controls,
		Background,
		BackgroundVariant,
		useSvelteFlow,
		useNodesInitialized,
		useStore,
		SvelteFlowProvider
	} from '@xyflow/svelte';
	import '@xyflow/svelte/dist/style.css';

	import { theme, models, tools, functions } from '$lib/stores';
	import BaseNode from './Nodes/BaseNode.svelte';
	import Sidebar from '$lib/components/icons/Sidebar.svelte';
	import Plus from '$lib/components/icons/Plus.svelte';
	import Sparkles from '$lib/components/icons/Sparkles.svelte';
	import CloudArrowUp from '$lib/components/icons/CloudArrowUp.svelte';

	const i18n = getContext('i18n');

	export let workflow = null;
	export let onSave: (data: any) => void;

	const nodeTypes = {
		base: BaseNode
	};

	const nodes = writable(workflow?.nodes || [
		{
			id: 'trigger-1',
			type: 'base',
			data: { label: 'Manual Trigger', type: 'trigger', icon: '⚡' },
			position: { x: 250, y: 50 }
		}
	]);

	const edges = writable(workflow?.edges || []);

	let flowInstance = null;

	const onConnect = (params) => {
		edges.update((e) => [...e, { ...params, id: `e-${params.source}-${params.target}`, animated: true }]);
	};

	const addNode = (type: string) => {
		const id = `${type}-${Date.now()}`;
		const newNode = {
			id,
			type: 'base',
			data: { 
				label: `New ${type}`, 
				type, 
				icon: type === 'model' ? '🧠' : type === 'tool' ? '🛠️' : type === 'logic' ? '⚖️' : '📦' 
			},
			position: { x: Math.random() * 400, y: Math.random() * 400 }
		};
		nodes.update((n) => [...n, newNode]);
	};

	const saveWorkflow = () => {
		onSave({
			nodes: $nodes,
			edges: $edges
		});
	};
</script>

<div class="flex flex-col w-full h-full bg-gray-50 dark:bg-gray-950 overflow-hidden relative">
	<!-- Toolbar -->
	<div class="absolute top-4 left-4 z-10 flex gap-2">
		<div class="p-1 rounded-2xl bg-white/80 dark:bg-gray-900/80 backdrop-blur-md border border-gray-100 dark:border-gray-800 shadow-xl flex gap-1">
			<button
				class="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-xl transition flex flex-col items-center gap-1 group"
				on:click={() => addNode('model')}
				title="Add Model"
			>
				<div class="text-xl">🧠</div>
				<span class="text-[10px] font-bold text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white uppercase tracking-tighter">Model</span>
			</button>
			<button
				class="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-xl transition flex flex-col items-center gap-1 group"
				on:click={() => addNode('tool')}
				title="Add Tool"
			>
				<div class="text-xl">🛠️</div>
				<span class="text-[10px] font-bold text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white uppercase tracking-tighter">Tool</span>
			</button>
			<button
				class="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-xl transition flex flex-col items-center gap-1 group"
				on:click={() => addNode('logic')}
				title="Add Logic"
			>
				<div class="text-xl">⚖️</div>
				<span class="text-[10px] font-bold text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white uppercase tracking-tighter">Logic</span>
			</button>
		</div>
	</div>

	<!-- Actions -->
	<div class="absolute top-4 right-4 z-10 flex gap-2">
		<button
			class="px-4 py-2 bg-black text-white dark:bg-white dark:text-black rounded-2xl shadow-xl font-medium text-sm flex items-center gap-2 hover:scale-105 transition"
			on:click={saveWorkflow}
		>
			<CloudArrowUp className="size-4" />
			{$i18n.t('Save Workflow')}
		</button>
		<button
			class="px-4 py-2 bg-green-600 text-white rounded-2xl shadow-xl font-medium text-sm flex items-center gap-2 hover:scale-105 transition"
			on:click={() => toast.info('Workflow test started...')}
		>
			<Sparkles className="size-4" />
			{$i18n.t('Test Run')}
		</button>
	</div>

	<div class="flex-1 w-full h-full border border-gray-100/10 rounded-3xl overflow-hidden shadow-inner">
		<SvelteFlow
			{nodes}
			{edges}
			{nodeTypes}
			on:connect={(e) => onConnect(e.detail)}
			fitView
			colorMode={$theme.includes('dark') ? 'dark' : 'light'}
		>
			<Background variant={BackgroundVariant.Dots} gap={20} size={1} />
			<Controls />
		</SvelteFlow>
	</div>
</div>

<style>
	:global(.svelte-flow__node) {
		cursor: grab;
	}
	:global(.svelte-flow__node:active) {
		cursor: grabbing;
	}
</style>
