<script>
  window.watsonAssistantChatOptions = {
    integrationID: "3f10e2e8-7169-49a7-a60b-9f74d96acf9e", // The ID of this integration.
    region: "eu-de", // The region your integration is hosted in.
    serviceInstanceID: "c3fcb8e2-01d4-4309-9f36-ecc2152d022a", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
