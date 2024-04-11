<script>
	import { onMount } from "svelte";
	import { GET } from "./transactions/+server";
	import TransactionTable from "$lib/components/transactionTable.svelte";
  import TopAppBar, { Section, Title } from '@smui/top-app-bar'

  /**
	 * @type {any}
	 */
  let transactions;
  onMount(async () => {
    transactions = await GET()
  })

</script>

<TopAppBar variant="static">
  <Section>
    <Title>Kulutin</Title>
  </Section>
</TopAppBar>
<TransactionTable transactions={transactions}></TransactionTable>