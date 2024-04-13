export type TransactionForm = {
	date: string;
	merchant: string;
	total: number;
	category_id: number;
};

export type Transaction = {
	date: string;
	merchant: string;
	total: number;
	category_name: string;
	category_id: number;
	id: number;
};
