<script>
  /**
	 * @type {any}
	 */
  export let transactions = [];

  import DataTable, { Head, Body, Row, Cell } from '@smui/data-table';
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
    {#each transactions as transaction}
      <Row>
        <Cell>{transaction.date}</Cell>
        <Cell>{transaction.merchant}</Cell>
        <Cell>{transaction.total}</Cell>
        <Cell>{transaction.category_id}</Cell>
      </Row>
    {/each}
  </Body>
</DataTable>