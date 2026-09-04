
(()=>{
  const ready=()=>{
    const nav=document.querySelector('.gh-nav'), menu=document.querySelector('.gh-menu-toggle');
    if(nav&&menu){
      menu.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
      nav.querySelectorAll('.gh-nav__toggle').forEach(btn=>btn.addEventListener('click',()=>{const item=btn.closest('.gh-nav__item');const open=item.classList.toggle('is-open');btn.setAttribute('aria-expanded',String(open));}));
      document.addEventListener('click',e=>{if(window.innerWidth<=900 && !nav.contains(e.target) && !menu.contains(e.target)){nav.classList.remove('is-open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');}});
      document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('is-open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');nav.querySelectorAll('.gh-nav__item.is-open').forEach(x=>x.classList.remove('is-open'));menu.focus();}});
      window.addEventListener('resize',()=>{if(window.innerWidth>900){nav.classList.remove('is-open');menu.setAttribute('aria-expanded','false');nav.querySelectorAll('.gh-nav__item.is-open').forEach(x=>x.classList.remove('is-open'));}}, {passive:true});
    }
    const top=document.querySelector('.gh-top');
    if(top){const update=()=>top.classList.toggle('is-visible',window.scrollY>500);window.addEventListener('scroll',update,{passive:true});update();top.addEventListener('click',e=>{e.preventDefault();window.scrollTo({top:0,behavior:'smooth'});});}
    document.querySelectorAll('[data-contact-form]').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();const hp=form.querySelector('[name=website]');if(hp&&hp.value)return;const data=new FormData(form),name=(data.get('name')||'').trim(),email=(data.get('email')||'').trim(),subject=(data.get('subject')||'').trim(),message=(data.get('message')||'').trim();const body=['Name: '+name,'Email: '+email,'','Message:',message].join('\n');const mailto='mailto:sales@greaterheight.tech?subject='+encodeURIComponent(subject||'Website Enquiry')+'&body='+encodeURIComponent(body);const status=form.querySelector('[data-form-status]');if(status){status.textContent='Your email application will open so you can review and send the enquiry.';status.setAttribute('role','status');}window.location.href=mailto;}));
    document.querySelectorAll('a[href="#"]').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));
    document.querySelectorAll('img:not([loading])').forEach((img,i)=>{if(i>2)img.loading='lazy';img.decoding='async';});
  };
  document.readyState==='loading'?document.addEventListener('DOMContentLoaded',ready):ready();
})();
