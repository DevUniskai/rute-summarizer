// function cpy(text) {
// 	navigator.clipboard.writeText(text)
// }  

async function cpy(text) {
  try {
    await navigator.clipboard.writeText(text);
    console.log('Page URL copied to clipboard');
  } catch (err) {
    console.error('Failed to copy: ', err);
  }
}