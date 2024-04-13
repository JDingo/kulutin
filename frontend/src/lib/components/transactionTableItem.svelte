<script lang="ts">
	import type { Category } from '$lib/types/Category';
	import type { Transaction } from '$lib/types/Transaction';
	import Button, { Icon, Label } from '@smui/button';
	import { Cell, Row } from '@smui/data-table';
	import List, { Item } from '@smui/list';
	import Menu from '@smui/menu';
	import Select, { Option } from '@smui/select';
	import Textfield from '@smui/textfield';
	import { createEventDispatcher } from 'svelte';

	export let transaction: Transaction;
	let editableTranscation = transaction;

	export let categories: Category[];

	const dispatch = createEventDispatcher<{ edit: Transaction; delete: Transaction }>();

	const dispatchEdit = () => {
		dispatch('edit', editableTranscation);
		editState = !editState;
	};

	const dispatchDelete = () => {
		dispatch('delete', transaction);
	};

	let editState = false;

	let menu: Menu;
</script>

{#if editState}
	<Row>
		<Cell>
			<Textfield bind:value={editableTranscation.date} label="Date" required></Textfield>
		</Cell>
		<Cell>
			<Textfield bind:value={editableTranscation.merchant} label="Merchant" required />
		</Cell>
		<Cell>
			<Textfield bind:value={editableTranscation.total} label="Total" required />
		</Cell>
		<Cell>
			<Button on:click={() => menu.setOpen(true)}>
				<Label>{editableTranscation.category_name}</Label>
			</Button>
		</Cell>
		<Cell>
			<Button on:click={dispatchEdit}>
				<Icon class="material-icons">save</Icon><Label>Save</Label></Button
			></Cell
		>
	</Row>
	<Menu bind:this={menu}>
		<List>
			{#each categories as category (category.id)}
				<Item
					on:SMUI:action={() => {
						editableTranscation.category_id = category.id;
						editableTranscation.category_name = category.category_name;
					}}>{category.category_name}</Item
				>
			{/each}
		</List>
	</Menu>
{:else}
	<Row>
		<Cell>{transaction.date}</Cell>
		<Cell>{transaction.merchant}</Cell>
		<Cell>{transaction.total}</Cell>
		<Cell>{transaction.category_name}</Cell>
		<Cell>
			<Button on:click={() => (editState = true)}>
				<Icon class="material-icons">edit</Icon><Label>Edit</Label></Button
			></Cell
		>
		<Cell
			><Button color="primary" variant="unelevated" on:click={dispatchDelete}
				><Icon class="material-icons">delete</Icon>
				<Label>Delete</Label>
			</Button></Cell
		>
	</Row>
{/if}
