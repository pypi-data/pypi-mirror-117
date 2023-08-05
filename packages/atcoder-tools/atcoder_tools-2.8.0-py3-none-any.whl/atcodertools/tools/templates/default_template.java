import java.io.*;
import java.util.*;

class Main {
    {% if mod %}
    static final long MOD = {{ mod }};
    {% endif %}
    {% if yes_str %}
    static final String YES = "{{ yes_str }}";
    {% endif %}
    {% if no_str %}
    static final String NO = "{{ no_str }}";
    {% endif %}

    // Generated by {{ atcodertools.version }} {{ atcodertools.url }}  (tips: You use the default template now. You can remove this line by using your custom template)
    public static void main(String[] args) throws Exception {
        {% if prediction_success %}
        {{ input_part }}
        solve({{ actual_arguments }});
        {% else %}
        // Failed to predict input format
        {% endif %}
    }

    {% if prediction_success %}
    static void solve({{ formal_arguments }}){

    }
    {% endif %}
}
