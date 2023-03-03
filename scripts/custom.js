$.getQueryParameters = function(str) {
  return (str || document.location.search).replace(/(^\?)/,'').split("&")
  .reduce(
    function(all,part){
      part=part.split("=");
      all[part[0]]=part[1];
      return all;
    },
    {}
  );
};
