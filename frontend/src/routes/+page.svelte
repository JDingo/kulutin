<script>
	import { onMount } from 'svelte';
	import { GET_CATEGORIES, GET_TRANSACTIONS, POST_TRANSACTION } from './api/+server';
	import TransactionTable from '$lib/components/transactionTable.svelte';
	import TopAppBar, { Section, Title } from '@smui/top-app-bar';
	import Button, { Label, Icon } from '@smui/button';
	import Textfield from '@smui/textfield';
	import Select, { Option } from '@smui/select';
	/**
	 * @type {any}
	 */
	let transactions = [];
	onMount(async () => {
		transactions = await GET_TRANSACTIONS();
	});

	/**
	 * @type {any}
	 */
	let categories = [];
	onMount(async () => {
		categories = await GET_CATEGORIES();
	});

	let form_data = { date: '', merchant: '', total: '0.0', category_id: 0 };

	const handleSubmit = async (/** @type {{ preventDefault: () => void; }} */ e) => {
		e.preventDefault();

		const data = { ...form_data, total: parseFloat(form_data.total) };
		const response = await POST_TRANSACTION(data);

		transactions = [...transactions, response];
	};
</script>

<div class="outer">
	<div class="center">
		<TopAppBar variant="static">
			<Section>
				<Title>Kulutin</Title>
			</Section>
		</TopAppBar>
		<div class="content">
			<TransactionTable {transactions}></TransactionTable>
			<div>
				<form on:submit={handleSubmit}>
					<Textfield bind:value={form_data.date} label="Date" required>
						<Icon class="material-icons" slot="leadingIcon">event</Icon>
					</Textfield>

					<Textfield bind:value={form_data.merchant} label="Merchant" required />

					<Textfield bind:value={form_data.total} label="Total" required />
					<Select
						bind:value={form_data.category_id}
						label="Category"
						key={(category) => `${category ? category.id : 0}`}
					>
						{#each categories as category (category.category_name)}
							<Option value={category.id}>{category.category_name}</Option>
						{/each}
					</Select>
					<Button type="submit">
						<Label>Submit</Label>
					</Button>
				</form>
			</div>
		</div>
	</div>
</div>

<style>
	.outer {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		flex-direction: column;
	}

	.center {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 60%;
	}
	.content {
		display: flex;
		flex-direction: column;
	}
</style>
