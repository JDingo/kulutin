<script lang="ts">
	import type { Transaction } from '$lib/types/Transaction';
	import type { Category } from '$lib/types/Category';

	export let transactions: Transaction[] = [];
	export let categories: Category[] = [];

	import DataTable, { Head, Body, Row, Cell, Label } from '@smui/data-table';
	import TransactionTableItem from './transactionTableItem.svelte';
</script>

<DataTable table$aria-label="transactions list">
	<Head>
		<Row>
			<Cell>Date</Cell>
			<Cell>Merchant</Cell>
			<Cell>Total</Cell>
			<Cell>Category</Cell>
		</Row>
	</Head>
	<Body>
		{#each transactions as transaction (transaction.id)}
			<TransactionTableItem {transaction} {categories} on:edit on:delete />
		{/each}
	</Body>
</DataTable>
