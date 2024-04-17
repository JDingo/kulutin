<script lang="ts">
	import { onMount } from 'svelte';
	import {
		DELETE_TRANSACTION,
		GET_CATEGORIES,
		GET_TRANSACTIONS,
		POST_TRANSACTION,
		PUT_TRANSACTION
	} from '../api/server';
	import TransactionTable from '$lib/components/transactionTable.svelte';
	import TopAppBar, { Section, Title } from '@smui/top-app-bar';
	import Button, { Label, Icon } from '@smui/button';
	import Textfield from '@smui/textfield';
	import Select, { Option } from '@smui/select';
	import type { Transaction } from '$lib/types/Transaction';
	import type { Category } from '$lib/types/Category';

	let transactions: Transaction[] = [];
	let categories: Category[] = [];

	onMount(async () => {
		transactions = await GET_TRANSACTIONS();
		categories = await GET_CATEGORIES();

		transactions = transactions.map((transaction) => {
			const category_name = categories.find(
				(category) => category.id == transaction.category_id
			)?.category_name;

			transaction.category_name = category_name ? category_name : 'Non-defined';

			return transaction;
		});

		transactions = transactions.sort((a, b) => a.id - b.id);
	});

	let form_data = { date: '', merchant: '', total: '0.0', category_id: 0 };

	const handleSubmit = async (e: Event) => {
		e.preventDefault();

		const data = { ...form_data, total: parseFloat(form_data.total) };
		const response = await POST_TRANSACTION(data);

		response.category_name = categories.find(
			(category) => category.id == response.category_id
		)?.category_name;
		response.total = parseFloat(response.total);

		transactions = [...transactions, response];
	};

	const handleEdit = async (e: CustomEvent<Transaction>) => {
		const transaction = e.detail;
		const response = await PUT_TRANSACTION(transaction);

		let newTransactions = transactions.filter((transaction) => transaction.id != response.id);
		response.category_name = categories.find(
			(category) => category.id == response.category_id
		)?.category_name;
		response.total = parseFloat(response.total);
		newTransactions = [...newTransactions, response];
		newTransactions.sort((a, b) => a.id - b.id);

		transactions = newTransactions;
	};

	const handleDelete = async (e: CustomEvent<Transaction>) => {
		const transaction = e.detail;
		const response = await DELETE_TRANSACTION(transaction);

		let newTransactions = transactions.filter((transaction) => transaction.id != response.id);
		newTransactions.sort((a, b) => a.id - b.id);

		transactions = newTransactions;
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
			<TransactionTable
				{transactions}
				{categories}
				on:edit={(transaction) => handleEdit(transaction)}
				on:delete={(transaction) => handleDelete(transaction)}
			></TransactionTable>
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
