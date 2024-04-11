import { baseUrl } from '$lib/api';

export async function GET() {
	const response = await fetch(`${baseUrl}/transactions`, {
		method: 'GET'
	}).then((res) => res.json());

	return response;
}
