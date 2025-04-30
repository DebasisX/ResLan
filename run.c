#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input.json> <output_base_name>\n", argv[0]);
        return 1;
    }

    const char *json_in = argv[1];
    const char *out_base = argv[2];

    /* build command string: python3 resume.py input.json output_base.pdf */
    char cmd[4096];
    int n = snprintf(cmd, sizeof(cmd),
                     "python3 resume.py %s %s.pdf",
                     json_in, out_base);
    if (n < 0 || n >= (int)sizeof(cmd)) {
        fprintf(stderr, "Command too long or encoding error\n");
        return 1;
    }

    int rc = system(cmd);
    if (rc == -1) {
        fprintf(stderr, "Failed to launch python: %s\n", strerror(errno));
        return 1;
    }
    /* return the exit status of the Python process */
    return WEXITSTATUS(rc);
}
