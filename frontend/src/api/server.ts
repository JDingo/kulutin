import { baseUrl } from '$lib/api';
import type { Category } from '$lib/types/Category';
import type { Transaction, TransactionForm } from '$lib/types/Transaction';

export async function GET_TRANSACTIONS() {
	const response = await fetch(`${baseUrl}/transactions`, {
		method: 'GET'
	}).then((res) => res.json());

	return response;
}

export async function POST_TRANSACTION(data: TransactionForm) {
	const response = await fetch(`${baseUrl}/transactions`, {
		method: 'POST',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	}).then((res) => res.json());

	return response;
}

export async function GET_CATEGORIES(): Promise<Category[]> {
	const response = await fetch(`${baseUrl}/categories`, {
		method: 'GET'
	}).then((res) => res.json());

	return response;
}

export async function PUT_TRANSACTION(transaction: Transaction) {
	const response = await fetch(`${baseUrl}/transactions/${transaction.id}`, {
		method: 'PUT',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(transaction)
	}).then((res) => res.json());

	return response;
}

export async function DELETE_TRANSACTION(transaction: Transaction) {
	const response = await fetch(`${baseUrl}/transactions/${transaction.id}`, {
		method: 'DELETE',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(transaction)
	}).then((res) => res.json());

	return response;
}
