<script setup>
import { useForm } from 'vee-validate';

const { handleSubmit } = useForm({
    validationSchema: registrationSchema,
});


const onSubmit = handleSubmit(async (values, actions) => {

    console.log(values); // Send data to API
    
    // Reset the form and the field values to their initial values
    actions.resetForm();

    registerUser(values);

});


</script>

<template>
    <form @submit="onSubmit">
        <div class="join join-vertical">

            <!-- Username Field -->
            <div class="join-item py-1">
               <UIInputField name="username" labelName="Username" placeholder="Enter a username"/>
             </div>
             
             <!-- Password Field -->
            <div class="join-item py-1">
               <UIInputField name="password" type="password" labelName="Password:" placeholder="Enter a Password" />
             </div>

             <!-- Confirm Password Field -->
            <div class="join-item py-1">
               <UIInputField name="confirmPassword" type="password" labelName="Confirm Password:" placeholder="Re-enter password"/>
             </div>

            <!-- Submit Button -->
            <div class="py-5">
                <button type="submit" class="btn btn-neutral btn-wide">Create Account</button>
            </div>

        </div>
    </form>
</template>