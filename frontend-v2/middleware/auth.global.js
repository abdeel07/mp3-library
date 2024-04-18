export default defineNuxtRouteMiddleware((to) => {
  const { authenticated } = storeToRefs(useAuthStore());
  const { userData } = storeToRefs(useAuthStore());
  const token = useCookie("token");

  // Check if token exists, before updating that state
  if (token.value) {
    authenticated.value = true;
  }

  // if token exists and url is /login redirect to homepage
  if (token.value && to?.path === 'profile') {
    return navigateTo(`profile`);
  }

  // if token doesn't exist redirect to log in
  if (!token.value && to?.path !== '/') {
    abortNavigation();
    return navigateTo('/');
  } 

  // if token exists, redirect to profile page after login   
  if (token.value && to?.path === '/') {
    return navigateTo('profile');
  }


});
