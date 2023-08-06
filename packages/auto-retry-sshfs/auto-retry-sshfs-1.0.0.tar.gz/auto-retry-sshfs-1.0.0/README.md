
# Idea

Allows you to run sshfs in such a way that you don't have to worry about it crashing for whatever reason. Automatically will unmount and remount your sshfs drive if it crashes. Great for if you're using sshfs over a noisy connection or over kerebros or something.

# Usage

```
auto-retry-sshfs --source-server user@server --source-path /path --target-path /path
```