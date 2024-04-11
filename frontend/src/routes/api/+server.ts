import { baseUrl } from '$lib/api';

export async function GET_TRANSACTIONS() {
	const response = await fetch(`${baseUrl}/transactions`, {
		method: 'GET'
	}).then((res) => res.json());

	return response;
}

export async function POST_TRANSACTION(data) {
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

export async function GET_CATEGORIES() {
	const response = await fetch(`${baseUrl}/categories`, {
		method: 'GET'
	}).then((res) => res.json());

	return response;
}
