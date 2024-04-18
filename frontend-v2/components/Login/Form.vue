<script setup>
import { useForm } from "vee-validate";

const authStore = useAuthStore();

const { handleSubmit } = useForm({
  validationSchema: loginSchema,
});

const onSubmit = handleSubmit(async (values, actions) => {
  try {
    await authStore.authenticateUser(values.username, values.password);

    if (authStore.authenticated) {
      console.log("Login Successful!");
      navigateTo(`/profile`);
      actions.resetForm();
    } else {
      console.error('Login Failed!');
    }

  } catch (error) {
    console.error("An error occurred:", error);
  }
});

</script>

<template>
  <form @submit="onSubmit">
    <div class="join join-vertical">
      <!-- Username Field -->
      <div class="join-item py-1">
        <UIInputField name="username" labelName="Username" placeholder="Enter a username" />
      </div>

      <!-- Password Field -->
      <div class="join-item py-1">
        <UIInputField name="password" type="password" labelName="Password:" placeholder="Enter a Password" />
      </div>

      <!-- Submit Button -->
      <div class="py-5">
        <button type="submit" class="btn btn-neutral btn-wide">Login</button>
      </div>
    </div>
  </form>
</template>
