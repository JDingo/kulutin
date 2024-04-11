<script>
	import { onMount } from "svelte";
	import { GET } from "./transactions/+server";
	import TransactionTable from "$lib/components/transactionTable.svelte";

  /**
	 * @type {any}
	 */
  let transactions;
  onMount(async () => {
    transactions = await GET()
  })

</script>

<h1>Kulutin</h1>
<TransactionTable transactions={transactions}></TransactionTable>