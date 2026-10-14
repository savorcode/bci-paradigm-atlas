# Deploying the project page

The project page (`website/`) is a static site. It is served from the company server at **atlas.mentiscale.com**.

1. **DNS (Namecheap → Advanced DNS):** add an `A Record`, host `atlas`, value = the server's public IP, TTL Automatic.
   If the domain's nameservers are not Namecheap BasicDNS, add the record at the DNS provider in use instead.
2. **Server:** `git clone https://github.com/savorcode/bci-paradigm-atlas.git /var/www/bci-paradigm-atlas`.
3. **Nginx:** copy `deploy/nginx-atlas.conf` to `/etc/nginx/conf.d/atlas.conf`, then `nginx -t && systemctl reload nginx`.
4. **HTTPS:** `certbot --nginx -d atlas.mentiscale.com` (free Let's Encrypt certificate, renews automatically).
5. **Updates:** add `deploy/update.sh` to cron (every 10 minutes). Each merge to `main` appears on the site within ten minutes.

For a server in a mainland-China region, the domain needs an ICP filing (备案) before ports 80/443 are reachable; a Hong Kong or overseas region does not.
The page loads no external resources: Latin fonts are in `website/assets/fonts` (SIL Open Font License) and Chinese text uses the system font.
