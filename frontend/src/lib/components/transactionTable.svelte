<script>
  /**
	 * @type {any}
	 */
  export let transactions = [];
</script>

<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>Merchant</th>
      <th>Total</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    {#each transactions as transaction}
      <th>{transaction.date}</th>
      <td>{transaction.merchant}</td>
      <td>{transaction.total}</td>
      <td>{transaction.category_id}</td>
    {/each}
  </tbody>
</table>