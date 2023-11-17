<script setup>
import Sidebar from '@/components/Sidebar.vue';
</script>
<template>
	<Sidebar />
	<main id="Home-page">
		<h1>Home</h1>
		<p>This is the home page</p>
	</main>
</template>

<script>
export default {
	components: {
		Sidebar,
	}
}
</script>