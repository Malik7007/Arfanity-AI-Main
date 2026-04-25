<script lang="ts">
	import { Handle, Position } from '@xyflow/svelte';
	import { getContext } from 'svelte';
	
	const i18n = getContext('i18n');

	export let data;
	export let selected = false;

	$: type = data.type || 'model';
	$: icon = data.icon || '🧠';
</script>

<div
	class="px-4 py-3 rounded-2xl bg-white dark:bg-gray-900 border {selected
		? 'border-black dark:border-white ring-1 ring-black dark:ring-white'
		: 'border-gray-100 dark:border-gray-800'} shadow-lg transition-all min-w-[180px]"
>
	<Handle type="target" position={Position.Top} class="w-3 h-3 bg-gray-400 border-2 border-white dark:border-gray-900" />
	
	<div class="flex items-center gap-3">
		<div class="text-2xl">{icon}</div>
		<div class="flex-1 overflow-hidden">
			<div class="text-xs font-bold text-gray-500 uppercase tracking-wider leading-none mb-1">
				{type}
			</div>
			<div class="text-sm font-medium truncate">
				{data.label || 'New Node'}
			</div>
		</div>
	</div>

	{#if data.description}
		<div class="mt-2 text-[10px] text-gray-400 line-clamp-2">
			{data.description}
		</div>
	{/if}

	<Handle type="source" position={Position.Bottom} class="w-3 h-3 bg-gray-400 border-2 border-white dark:border-gray-900" />
</div>
