<script lang="ts">
	import { models, settings } from '$lib/stores';
	import equal from 'fast-deep-equal';

	const LOCKED_MODEL_ID = 'unity-rag-assistant';

	export let selectedModels = [LOCKED_MODEL_ID];
	export let disabled = false;
	export let showSetDefault = true;

	$: lockedModel = $models.find((model) => model.id === LOCKED_MODEL_ID);
	$: if (!equal(selectedModels, [LOCKED_MODEL_ID])) {
		selectedModels = [LOCKED_MODEL_ID];
	}
</script>

<div class="flex flex-col w-full items-start">
	<div class="flex w-full max-w-fit">
		<div class="overflow-hidden w-full">
			<div class="max-w-full {($settings?.highContrastMode ?? false) ? 'm-1' : 'mr-1'}">
				<div
					class="flex items-center min-h-8 max-w-full rounded-lg px-2.5 py-1.5 text-sm font-medium text-gray-800 dark:text-gray-100 bg-gray-50 dark:bg-gray-850 border border-gray-100 dark:border-gray-800 select-none"
					aria-disabled="true"
				>
					<span class="truncate">{lockedModel?.name ?? LOCKED_MODEL_ID}</span>
				</div>
			</div>
		</div>
	</div>
</div>
